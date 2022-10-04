from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ListingForm

from .models import User, Listing, Watchlist, Category, Bid, Comment

register_url ="auctions/register.html"
#@login_required(login_url='/login') i will add this to the place_bid method
def index(request):
    return render(request, "auctions/index.html",{
        "listings" : Listing.objects.filter(is_active=True),
    })

def user_is_creator(user, listing):
    if user and user == listing.user:
        return True

def is_in_watchlist(user, listing):
    user_listing_ids = Watchlist.objects.filter(user = user).values("listings") 
    user_listings = Listing.objects.filter(id__in = user_listing_ids)
    if listing in user_listings:
        return True
    return False

def get_winner(listing):
    try: 
        bid = Bid.objects.get(listing=listing)
        return bid.user 

    except Bid.DoesNotExist: 
        return listing.user

@login_required(login_url='/login')
def view_listing(request, listing_id):
    if Listing.objects.filter(id=listing_id).exists():
        listing = Listing.objects.get(pk=listing_id)
        user = request.user
        winner = None
        if not listing.is_active:
            winner = get_winner(listing)
        return render(request, "auctions/view_listing.html", {
            "listing" : listing,
            "message" : None,
            "in_watchlist" : is_in_watchlist(user, listing),
            "created_by_user": user_is_creator(user, listing),
            "winner" : winner,
            "comments": Comment.objects.filter(listing_id=listing_id),
            "user" : user,
            
        })
    return render(request, "auctions/view_listing.html", {
        "message" : "Invalid listing id.",
    })
 
def view_watchlist(request, user_id):
    user = User.objects.get(id = user_id)
    user_listing_ids = Watchlist.objects.filter(user = user).values("listings") 
    user_listings = Listing.objects.filter(id__in = user_listing_ids)
    return render(request, "auctions/view_watchlist.html",{
        "watchlist_listings": user_listings,
    }) 

@login_required(login_url='/login')
def add_to_watchlist(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    user = request.user
    watchlist_item = Watchlist.objects.filter(user = user, listings = listing)
    if watchlist_item:
        watchlist_item = Watchlist.objects.get(user = user, listings = listing)
        watchlist_item.save()
    else:
        Watchlist.objects.create(user = user, listings = listing)
    return HttpResponseRedirect(reverse("view_listing", args=[listing_id],))

@login_required(login_url='/login')
def remove_from_watchlist(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    user = request.user
    watchlist_item = Watchlist.objects.filter(user = user, listings = listing)
    if watchlist_item:
        watchlist_item = Watchlist.objects.get(user = user, listings = listing)
        watchlist_item.delete()
    else:
        Watchlist.objects.create(user = user, listings = listing)
    return HttpResponseRedirect(reverse("view_listing", args=[listing_id],))

@login_required(login_url='/login')
def create_listing(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.is_active = True
            form.save()
            return HttpResponseRedirect(reverse("view_listing", args=[form.id],))
    return render(request, "auctions/create_listing.html",{
        "form":form,
    })
@login_required(login_url='/login')
def place_bid(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(pk=listing_id)
        if listing.is_active:
            user = request.user
            cost = float(request.POST["cost"])
            listing.cost = cost
            listing.save()
            Bid.objects.create(listing = listing, cost = cost, user = user) 
        return HttpResponseRedirect(reverse("view_listing", args=[listing_id],))

@login_required(login_url='/login')
def close_bid(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(pk=listing_id)
        user = request.user
        if user_is_creator(user, listing):
            listing.is_active = False
            listing.save()
    return HttpResponseRedirect(reverse("view_listing", args=[listing_id],))

@login_required(login_url='/login')
def comment(request, listing_id):
    if request.method == "POST":
        user = request.user
        content = request.POST["content"]
        Comment.objects.create(content=content, user=user, listing_id=listing_id, user_id=user.id)
    return HttpResponseRedirect(reverse("view_listing", args=[listing_id],))  

@login_required(login_url='/login')
def select_category(request):
    if request.method == "POST":
        category_title = request.POST["category"]
        category = Category.objects.get(title=category_title)
        return render(request, "auctions/category.html",{
        "listings" : Listing.objects.filter(category=category, is_active=True),
        "category" : category_title,
        })
    HttpResponse("There was an error returning specific category's listings")

def select_category_get(request, category_id):
    if request.method == "GET":
        requested_category = Category.objects.get(id=category_id)
        return render(request, "auctions/category.html", {
            "listings" : Listing.objects.filter(category = requested_category),
            "category" : requested_category.title,
        })
    HttpResponse("This was supposed to be a GET request NOT POST")
def view_all_categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "auctions/select_category.html", {
            "categories" : categories,
        })
    HttpResponse("There was an error tring to view all categories")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, register_url, {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, register_url, {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, register_url)
