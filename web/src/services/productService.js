import http from '../configs/http';

export function getProducts() {
  return http.get('products/')
}