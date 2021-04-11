import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WelcomeHangmanComponent } from './welcome-hangman/welcome-hangman.component'
import { ChooseLanguageComponent } from './choose-language/choose-language.component'

const routes: Routes = [
  { path: '', component:  WelcomeHangmanComponent },
  { path: 'choose-language', component:  ChooseLanguageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
