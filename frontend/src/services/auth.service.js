import { HttpService } from './http.service';
import { getFingerprint } from '../utils/get-fingerprint';
import AuthStore from "../stores/auth.store";

class AuthService {
    
    static async login(email, password) {
        try {
            const http = new HttpService();
            const fingerprint = await getFingerprint();
            const response = await http.post(
                '/auth/login',
                { email, password, fingerprint },
                { withCredentials: true }
            );
            await AuthStore.setAuthData(response.data.access_token);
        } catch (error) {
            throw new Error(error);
        }
    }

    static async register(email, password) {
        try {
            const http = new HttpService();
            await http.post(
                '/auth/register',
                { email, password },
                { withCredentials: true }
            );
        } catch (error) {
            throw new Error(error);
        }
    }

    static async refreshTokens() {
        try {
            const http = new HttpService({});
            const fingerprint = await getFingerprint();
            const response = await http.post(
                '/auth/refresh-token',
                { fingerprint },
                { withCredentials: true }
            );
            await AuthStore.setAuthData(response.data.access_token);
        } catch (error) {
            AuthStore.resetAuthData();
        }
    }

    static async logout() {
        const http = new HttpService({ withAuth: true });
        await http.post('/auth/logout');
        AuthStore.resetAuthData();
    }

    static isAccessTokenExpired() {
        const expDate = AuthStore.getExpiresAt() - 10;
        const nowDate = Math.floor(new Date().getTime() / 1000);
        return expDate <= nowDate;
      }
    
      static isAuthenticated() {
        if(!AuthStore.getAuthorized()){
            return false
        }
        return this.isAccessTokenExpired()
          ? this.refreshTokens().then(() => AuthStore.getAccessToken())
          : Boolean(AuthStore.getAccessToken()) && !this.isAccessTokenExpired();
      }
    
      static getAccessToken() {
        if (!this.isAuthenticated()) throw new Error();
        return AuthStore.getAccessToken();
      }
}


export default AuthService;