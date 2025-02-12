import { Component, EventEmitter, Input, Output } from '@angular/core';
import { BookService } from '../../services/book.service';

@Component({
  selector: 'app-book-form',
  templateUrl: './book-form.component.html',
  styleUrls: ['./book-form.component.css']
})
export class BookFormComponent {
  @Input() book = { title: '', author: '', read: false, id: null };
  @Output() bookSaved = new EventEmitter<void>();

  constructor(private bookService: BookService) {}

  async saveBook() {
    if (this.book.id) {
      await this.bookService.updateBook(this.book.id, this.book);
    } else {
      await this.bookService.addBook(this.book);
    }
    this.bookSaved.emit();
    this.resetForm();
  }

  resetForm() {
    this.book = { title: '', author: '', read: false, id: null };
  }
}
