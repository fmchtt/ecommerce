import http, { getHeaders } from '../configs/http';

export function getCategories() {
  return http.get('category/');
}

export function createCategory(name) {
  return http.post('category/', { name: name }, { headers: getHeaders() });
}
