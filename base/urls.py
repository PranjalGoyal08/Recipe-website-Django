from django.urls import path
from . import views
from . views import HomeView, ArticleDetailView, AddIngridentView,UpdateRecipeView, DeleteRecipeView,SearchResultView, LikeView, UnlikeView
urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('addingrident/', AddIngridentView.as_view(), name="add_Ingrident"),
    path('article/edit/<int:pk>', UpdateRecipeView.as_view(), name="update-recipe"),
    path('article/<int:pk>/remove', DeleteRecipeView.as_view(), name="delete-recipe"),
    path('search/', SearchResultView.as_view(), name="search-recipe"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('unlike/<int:pk>', UnlikeView, name="unliked_post"),
    path('add_Recipe/', views.create_ingrident_recipe, name='add-recipe'),
    # path('add', views.AddRecipe.as_view(), name='recipe-add'),
]