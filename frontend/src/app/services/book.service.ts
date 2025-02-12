import { Injectable } from '@angular/core';
import axios from 'axios';

@Injectable({
  providedIn: 'root'
})
export class BookService {
  private apiUrl = 'http://127.0.0.1:5000/books';

  async getBooks() {
    const response = await axios.get(this.apiUrl);
    return response.data;
  }

  async addBook(book: any) {
    const response = await axios.post(this.apiUrl, book);
    return response.data;
  }

  async updateBook(id: string, book: any) {
    const response = await axios.put(`${this.apiUrl}/${id}`, book);
    return response.data;
  }

  async deleteBook(id: string) {
    await axios.delete(`${this.apiUrl}/${id}`);
  }
}
