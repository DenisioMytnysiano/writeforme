import { HttpService } from './http.service';

class PoetryService{

    static async getAllPoems(page, items_per_page){
        const http = HttpService({withAuth: false})
        const response = await http.get(`/poems/?page=${page}&count=${items_per_page}`);
        return response.data;
    }

    static async getMyPoems(page, items_per_page){
        const http = HttpService({withAuth: true})
        const response = await http.get(`/poems/mine?page=${page}&count=${items_per_page}`);
        return response.data;
    }

    static async getPoem(id) {
        const http = HttpService({withAuth: false})
        const response = await http.get(`/poems/${id}`);
        return response.data;
    }

    static async save(poem){
        const http = HttpService({withAuth: true})
        const response = await http.post("/poems/save", {
            title: poem.split("\n")[0].trim().replaceAll(",", ""),
            text: poem
        });
        return response.data; 
    }

    static async deletePoem(id){
        const http = HttpService({withAuth: true})
        const response = await http.delete(`/poems/${id}`);
        return response.data;
    }
}

export default PoetryService;