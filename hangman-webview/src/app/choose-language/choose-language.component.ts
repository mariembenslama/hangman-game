import { Component, OnInit } from '@angular/core';
import { ChooseLanguageService } from '../service/choose-language.service'

@Component({
  selector: 'app-choose-language',
  templateUrl: './choose-language.component.html',
  styleUrls: ['./choose-language.component.css']
})

export class ChooseLanguageComponent implements OnInit {

  languages: []

  constructor(
    private chooseLanguageService: ChooseLanguageService) {
  }
  

  ngOnInit() {
    this.chooseLanguageService.getLanguages().subscribe(data => {
      this.languages = data;
    })
  }


}
