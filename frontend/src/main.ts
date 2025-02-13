import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));


  export const environment = {
    production: false,
    apiUrl: 'http://flask_api:5000'  // Conexión con Flask dentro de Docker
  };
