import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import {RouterModule} from "@angular/router";
import { AppUsersComponent } from './app-users/app-users.component';
import {HttpClientModule} from "@angular/common/http";
import { UserDetailsComponent } from './user-details/user-details.component';
import {FormGroup, FormsModule, ReactiveFormsModule} from "@angular/forms";
import { AppProductComponent } from './app-product/app-product.component';


@NgModule({
  declarations: [
    AppComponent,
    NavBarComponent,
    AppUsersComponent,
    UserDetailsComponent,
    AppProductComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot([
      {path: 'users', component: AppUsersComponent},
      {path: 'users/:id', component: UserDetailsComponent},
      {path: 'products', component: AppProductComponent},
      {path: '', redirectTo:'products', pathMatch:'full'},
      {path: '**', redirectTo:'products', pathMatch:'full'}
    ]),
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
