import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-welcome-hangman',
  templateUrl: './welcome-hangman.component.html',
  styleUrls: ['./welcome-hangman.component.css']
})
export class WelcomeHangmanComponent implements OnInit {

  constructor( private router: Router ) {} 

  ngOnInit(): void {

  }

}
