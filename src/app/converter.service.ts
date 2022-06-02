import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ConverterService {

  rate:number=0;
  constructor(private http: HttpClient) {}

  get(){
    return this.http.get('https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=44cd0c0eb050f575949e');                           
    
  }
  
}
