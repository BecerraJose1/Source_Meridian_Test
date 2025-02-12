import { Component, OnInit } from '@angular/core';
import { BookService } from '../../services/book.service';

@Component({
  selector: 'app-book-list',
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.css']
})
export class BookListComponent implements OnInit {
  books: any[] = [];

  constructor(private bookService: BookService) {}

  async ngOnInit() {
    this.books = await this.bookService.getBooks();
  }

  async deleteBook(id: string) {
    await this.bookService.deleteBook(id);
    this.books = this.books.filter(book => book.id !== id);
  }
}
