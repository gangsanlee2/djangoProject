"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from admin.views import hello

urlpatterns = [
    path('', hello),
    path("basic/mlearn/", include('basic.mlearn.stroke.urls')),
    path("basic/dlearn/", include('basic.dlearn.dc_gan.urls')),
    path("basic/dlearn/", include('basic.dlearn.fashion.urls')),
    path("basic/mnist-number/", include('basic.dlearn.mnist_number.urls')),
    path("basic/nlp/", include('basic.nlp.urls')),
    path("basic/nlp/", include('basic.nlp.urls')),
    path("basic/dlearn/", include('basic.dlearn.iris.urls')),
    path("basic/webcrawler/", include('basic.webcrawler.urls')),
    path("blog/b_users/", include('blog.b_users.urls')),
    path("blog/comments/", include('blog.comments.urls')),
    path("blog/posts/", include('blog.posts.urls')),
    path("blog/tags/", include('blog.tags.urls')),
    path("blog/views/", include('blog.views.urls')),
    path("movie/cinemas/", include('movie.cinemas.urls')),
    path("movie/movies/", include('movie.movies.urls')),
    path("movie/showtimes/", include('movie.showtimes.urls')),
    path("movie/theater_tickets/", include('movie.theater_tickets.urls')),
    path("movie/theaters/", include('movie.theaters.urls')),
    path("security/users/", include('security.z_users.urls')),
    path("security/posts/", include('security.z_posts.urls')),
    path("shop/carts/", include('shop.carts.urls')),
    path("shop/categories/", include('shop.categories.urls')),
    path("shop/deliveries/", include('shop.deliveries.urls')),
    path("shop/orders/", include('shop.orders.urls')),
    path("shop/products/", include('shop.products.urls')),
]