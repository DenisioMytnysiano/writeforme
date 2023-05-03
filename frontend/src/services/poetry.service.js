import { HttpService } from './http.service';

const authHttp = new HttpService({ withAuth: true });
const anonymousHttp = new HttpService({ withAuth: false });

class PoetryService{
    static async get_all_poems(page, items_per_page){
        const response = await http.get(`/poems/page=${page}&count=${items_per_page}`);
        return response.data;
    }
}