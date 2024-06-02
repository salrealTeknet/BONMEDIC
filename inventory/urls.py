from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.StockListView.as_view(), name='inventory'),
    path('new', views.StockCreateView.as_view(), name='new-stock'),
    path('stock/<pk>/edit', views.StockUpdateView.as_view(), name='edit-stock'),
    path('stock/<pk>/delete', views.StockDeleteView.as_view(), name='delete-stock'),
    path('near-expiry-products/', views.near_expiry_products, name='near_expiry_products'),
    path('export-near-expiry-to-csv/', views.export_near_expiry_to_csv, name='export_near_expiry_to_csv'),

]