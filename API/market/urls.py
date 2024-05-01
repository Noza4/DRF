from django.urls import path
from market.views import CreateProduct, ProductInfo, ListingProducts, DeleteProduct, UpdateProduct

urlpatterns = [
    path("create/", CreateProduct.as_view(), name="create"),
    path("info/", ProductInfo.as_view(), name="info"),
    path("listing/", ListingProducts.as_view(), name="listing"),
    path("delete/<int:pk>/", DeleteProduct.as_view(), name="delete"),
    path("update/<int:pk>/", UpdateProduct.as_view(), name="update")
]
