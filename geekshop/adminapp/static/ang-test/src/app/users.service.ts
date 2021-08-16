import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {User, UserEdit} from "./user";
import {map, tap} from "rxjs/operators";


@Injectable({
  providedIn: 'root'
})
export class UsersService {
  private usersUrl = 'http://185.46.11.115/admin_staff/api/users';

  constructor(
    private http: HttpClient,) { }

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.usersUrl)
  };
  getUser(id:number): Observable<UserEdit[]> {

    return this.http.get<UserEdit[]>(this.usersUrl+'/'+id )
  }

  update(model: UserEdit, id: number): Observable<UserEdit> {
    return this.http.put<UserEdit>(this.usersUrl+'/'+id, model);
  }
}


