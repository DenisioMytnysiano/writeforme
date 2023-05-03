import { HttpService } from './http.service';

class GenerationService{
    static async generate(rhyming_scheme, text_prompt){
        const http = new HttpService({ withAuth: true });
        const response = await http.post("/model/generate", {rhyming_scheme: rhyming_scheme, text_prompt: text_prompt});
        return response.data.poem;
    }
}