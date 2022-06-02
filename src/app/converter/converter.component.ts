import { Component, OnInit } from '@angular/core';
import { ConverterService } from '../converter.service';
@Component({
  selector: 'app-converter',
  templateUrl: './converter.component.html',
  styleUrls: ['./converter.component.css']
})
export class ConverterComponent{

  amt : number =1;
  rate : number =77.57;
 constructor(private data: ConverterService) { }
  

  mul() : void{
   this.amt = this.amt*this.rate;
}

}
