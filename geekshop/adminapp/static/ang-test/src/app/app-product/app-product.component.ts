import {Component, OnInit} from '@angular/core';
import {Category, Products} from "../products";
import {UsersService} from "../users.service";
import {ProductService} from "../product.service";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-app-product',
  templateUrl: './app-product.component.html',
  styleUrls: ['./app-product.component.css']
})
export class AppProductComponent implements OnInit {
  category: Category[] | any;
  products: Products[] | any;
  tab: 0| any;


  constructor(
    private userService: ProductService,
    private route: ActivatedRoute
  ) {
  }

  ngOnInit(): void {
    this.getCategory()
    this.getProducts()

  }

  getCategory(): void {
    this.userService.getCategory().subscribe(data => this.category = data)
  }

  getProducts(id: any = null): void {
    console.log(id)
    if (id == null) {
      this.tab = 0
      this.userService.getProducts().subscribe(data => this.products = data)
    } else {
      this.tab = id
      this.userService.getProductsOfCategory(id).subscribe(data => this.products = data)
    }

  }

}
