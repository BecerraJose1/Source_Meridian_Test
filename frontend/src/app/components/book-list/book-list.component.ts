import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BookService } from '../../services/book.service';
import { BookFormComponent } from '../book-form/book-form.component';

@Component({
  selector: 'app-book-list',
  standalone: true,
  imports: [CommonModule, BookFormComponent],
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.css']
})
export class BookListComponent implements OnInit {
  books: any[] = [];
  selectedBook: any = { title: '', author: '', read: false, id: null };

  constructor(private bookService: BookService) {}

  async ngOnInit() {
    await this.loadBooks();
  }

  async loadBooks() {
    this.books = await this.bookService.getBooks();
    console.log("Books loaded:", this.books); 
  }

  selectBook(book: any) {
    this.selectedBook = { ...book };
  }

  async deleteBook(id: string) {
    await this.bookService.deleteBook(id);
    this.loadBooks();
  }
}
