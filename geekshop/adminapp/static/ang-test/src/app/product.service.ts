import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {User} from "./user";
import {Category, Products} from "./products";

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private categoryUrl = 'http://185.46.11.115/admin_staff/api/categories';
  private productsUrl = 'http://185.46.11.115/admin_staff/api/products';

  constructor(
    private http: HttpClient,) { }

  getCategory(): Observable<Category[]> {
    return this.http.get<Category[]>(this.categoryUrl)
  };

  getProducts(): Observable<Products[]>{
    return this.http.get<Products[]>(this.productsUrl)
  }
  getProductsOfCategory(id:any): Observable<Products[]>{
    return this.http.get<Products[]>(this.categoryUrl+'/'+id+'/products')
  }

}
