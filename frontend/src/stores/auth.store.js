
class AuthStore {

  setAuthData = (accessToken)  => {
    const { exp: expiresAt, sub } = JSON.parse(atob(accessToken.split('.')[1]));
    localStorage.setItem("expiresAt", expiresAt);
    localStorage.setItem("accessToken", accessToken);
    localStorage.setItem("sub", sub);
    localStorage.setItem("authorized", true);
  }

  resetAuthData = () => {
    localStorage.removeItem("expiresAt");
    localStorage.removeItem("accessToken");
    localStorage.removeItem("sub");
    localStorage.setItem("authorized", false)
  }

  getExpiresAt() {
    return localStorage.getItem("expiresAt");
  }

  getAccessToken(){
    return localStorage.getItem("accessToken");
  }

  getCurrentEmail(){
    return localStorage.getItem("sub");
  }

  getAuthorized(){
    return localStorage.getItem("authorized") === "true"
  }
}

const authStore = new AuthStore();
export default authStore;