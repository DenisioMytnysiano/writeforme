import axios from 'axios';
import AuthService from './auth.service';

const  REACT_APP_API_HOST  = "http://localhost:8081";

export const HttpService = function ({ withAuth } = false) {
  const instance = axios.create({ baseURL: "http://localhost:8081" });
  if (withAuth) {
    instance.interceptors.request.use(request => {
      if (AuthService.isAccessTokenExpired()) {
        AuthService.refreshTokens().catch(err => Promise.reject(err));
      }
      request.headers.authorization = AuthService.getAccessToken();
      request.withCredentials = true;
      return request;
    });
  }
  return instance;
};