from django.urls import path


from . import views

urlpatterns = [
    path("category/<str:category>", views.category, name="category_list"),
    path("categories", views.categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listing/<str:id>", views.listing, name="listing"),
    path("create", views.create, name="create"),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
