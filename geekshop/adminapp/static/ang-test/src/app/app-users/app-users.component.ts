import { Component, OnInit } from '@angular/core';
import {User} from "../user";
import {UsersService} from "../users.service";

@Component({
  selector: 'app-app-users',
  templateUrl: './app-users.component.html',
  styleUrls: ['./app-users.component.css'],
  providers: []

})
export class AppUsersComponent implements OnInit {
  users: User[]| any;

  constructor(private userService: UsersService) { }

  ngOnInit(): void {
    this.getUsers();
  }

  getUsers(): void {
    this.userService.getUsers().subscribe(user => this.users = user)
  }

}
