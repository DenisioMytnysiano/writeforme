import { HttpService } from './http.service';

class UserService{
    static async getUser(id){
        const http = new HttpService({ withAuth: false });
        const response = await http.get(`/users/${id}`);
        return response.data;
    }

    static async getUserByEmail(email){
        const http = new HttpService({ withAuth: false });
        const response = await http.get(`/users/by-email/${email}`);
        return response.data;
    }
}

export default UserService;