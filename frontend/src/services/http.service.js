import axios from 'axios';
import AuthService from './auth.service';

export const HttpService = function ({ withAuth } = false) {
  const instance = axios.create({ baseURL: "http://localhost:8081" });
  if (withAuth) {
    instance.interceptors.request.use(request => {
      if (AuthService.isAccessTokenExpired()) {
        AuthService.refreshTokens().catch(err => Promise.reject(err));
      }
      request.headers.authorization = `Bearer ${AuthService.getAccessToken()}`;;
      request.withCredentials = true;
      return request;
    });
  }
  return instance;
};