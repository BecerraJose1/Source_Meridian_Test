import { Injectable } from '@angular/core';
import axios from 'axios';

@Injectable({
  providedIn: 'root'
})
export class BookService {
  private apiUrl = 'http://127.0.0.1:5000';

  async getBooks() {
    const response = await axios.get(`${this.apiUrl}/books`);
    return response.data;
  }

  async getBook(id: string) {
    const response = await axios.get(`${this.apiUrl}/book/${id}`);
    return response.data;
  }

  async addBook(book: any) {
    const response = await axios.post(`${this.apiUrl}/add/book`, book);
    return response.data;
  }

  async updateBook(id: string, book: any) {
    const response = await axios.put(`${this.apiUrl}/edit/book/${id}`, book);
    return response.data;
  }

  async deleteBook(id: string) {
    await axios.delete(`${this.apiUrl}/delete/book/${id}`);
  }
}
