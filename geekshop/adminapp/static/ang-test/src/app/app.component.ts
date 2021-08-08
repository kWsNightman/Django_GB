import {Component, Output} from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Админка';

  showNavBar() {
    const showNavbar = (toggleId: any, navId: any, bodyId: any, headerId: any) => {
      const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId),
        bodypd = document.getElementById(bodyId),
        headerpd = document.getElementById(headerId)

      if (toggle && nav && bodypd && headerpd) {
          nav.classList.toggle('show')
          toggle.classList.toggle('bx-x')
          bodypd.classList.toggle('body-pd')
          headerpd.classList.toggle('body-pd')
      }
    }
    showNavbar('header-toggle', 'nav-bar', 'body-pd', 'header')

  }

}
