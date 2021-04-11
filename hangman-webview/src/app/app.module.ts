import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ChooseLanguageComponent } from './choose-language/choose-language.component';
import { WelcomeHangmanComponent } from './welcome-hangman/welcome-hangman.component';
import { Config } from 'src/api';

@NgModule({
  declarations: [
    AppComponent,
    ChooseLanguageComponent,
    WelcomeHangmanComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [Config],
  bootstrap: [AppComponent]
})
export class AppModule { }
