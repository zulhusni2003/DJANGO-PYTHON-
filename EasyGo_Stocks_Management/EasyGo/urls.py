from django.urls import path
from . import views

urlpatterns = [
     path("", views.signin, name="signin"),
     path("errorSignin", views.errorSignin, name="errorSignin"),
     path("dashboard", views.dashboard, name="dashboard"),
     path("product", views.product, name="product"),
     path("addProduct", views.addProduct, name="addProduct"),
     path("searchProduct", views.searchProduct, name="searchProduct"),
     path("stock", views.stock, name="stock"),
     path("productSection", views.productSection, name="productSection"),
     path("updateProduct/<str:productID>", views.updateProduct, name="updateProduct"),
     path("updateProduct/save_update_product/<str:productID>", views.save_update_product, name="save_update_product"),
     path("productDeletePage", views.productDeletePage, name="productDeletePage"),   
     path("deleteProduct/<str:productID>", views.deleteProduct, name="deleteProduct"),
     path("faqtable", views.faqtable, name="faqtable"),
     path("faq", views.faq, name="faq"),
     path("updatePassword", views.updatePassword, name="updatePassword.html"),
     path("staffTable", views.staffTable, name="staffTable"),
     path("newStaff", views.newStaff, name="newStaff"),
     path("staffDeletePage", views.staffDeletePage, name="staffDeletePage"),   
     path("deleteStaff/<str:staffID>", views.deleteStaff, name="deleteStaff"),
     path("staffSection", views.staffSection, name="staffSection"),
     path("updateStaff/<str:staffID>", views.updateStaff, name="updateStaff"),
     path("updateStaff/save_update_staff/<str:staffID>", views.save_update_staff, name="save_update_staff"),
     path("searchStaff", views.searchStaff, name="searchStaff"),
     ] 
