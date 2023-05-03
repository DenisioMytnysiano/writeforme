import { makeAutoObservable, runInAction } from 'mobx';

class AuthStore {
  constructor() {
    this.resetAuthData();
    makeAutoObservable(this);
  }

  async setAuthData(accessToken) {
    const { exp: expiresAt, sub: sub } = JSON.parse(atob(accessToken.split('.')[1]));
    runInAction(() => {
      Object.assign(this, { accessToken, expiresAt, sub });
    });
  }

  resetAuthData() {
    this.accessToken = this.expiresAt = this.sub = undefined;
  }
}

export default new AuthStore();