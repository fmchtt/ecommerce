import http from '../configs/http';

export function getProducts() {
  return http.get('products/');
}

export function getSingleProduct(id) {
  return http.get(`/products/${id}/`);
}

export function getProductsOfUser() {
  return http.get(`/products/created/me/`);
}
