from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing_id>", views.view_listing, name="view_listing"),
    path("view_watchlist/<int:user_id>", views.view_watchlist, name="view_watchlist"),
    path("add_to_watchlist/<int:listing_id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove_from_watchlist/<int:listing_id>", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("place_bid/<int:listing_id>", views.place_bid, name="place_bid"),
    path("close_bid/<int:listing_id>", views.close_bid, name="close_bid"),
    path("comment/<int:listing_id>", views.comment, name="comment"),
    path("select_category", views.select_category, name="select_category"),
    path("view_all_categories", views.view_all_categories, name="view_all_categories"),
]
