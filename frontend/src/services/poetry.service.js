import { HttpService } from './http.service';

class PoetryService{

    static async getAllPoems(page, items_per_page){
        const http = HttpService({withAuth: false})
        const response = await http.get(`/poems/?page=${page}&count=${items_per_page}`);
        return response.data;
    }

    static async getPoem(id) {
        const http = HttpService({withAuth: false})
        const response = await http.get(`/poems/${id}`);
        return response.data;
    }
}

export default PoetryService;