import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent implements OnInit {
  public activeItem: string | undefined ;
  constructor() { }

  ngOnInit(): void {
  }


  public onSelectItem(item: string): void {
    this.activeItem = item;
  }

}
