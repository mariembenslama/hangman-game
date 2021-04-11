import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Config } from 'src/api'

@Injectable({
  providedIn: 'root'
})
export class ChooseLanguageService {

  
  constructor(
    private http: HttpClient,
    private config: Config,
  ) {}

  public getLanguages(){
    return this.http.get<any>(this.config.host + this.config.getLanguageApi)
  }

}