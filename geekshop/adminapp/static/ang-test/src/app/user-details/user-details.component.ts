import {Input, Component, OnInit } from '@angular/core';
import {AppUsersComponent} from "../app-users/app-users.component";
import {UsersService} from "../users.service";
import {ActivatedRoute} from "@angular/router";
import {User, UserEdit} from "../user";
import {Subscription} from "rxjs";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-user-details',
  templateUrl: './user-details.component.html',
  styleUrls: ['./user-details.component.css']
})
export class UserDetailsComponent implements OnInit {
  i: User[]| any;
  form: FormGroup |any;
  aSub: Subscription|any;


  constructor(private route: ActivatedRoute,
              private userService: UsersService,
              private fb:FormBuilder
  ) {}

  ngOnInit(): void {


    this.form = this.fb.group({
      username : [null, [Validators.required, Validators.minLength(3)]],
      first_name: [null, [Validators.required]],
      last_name: [null, [Validators.required]],
    })

    this.getUser(this.route.snapshot.params.id)
  }

  getUser(id:number): void {
    this.aSub = this.userService.getUser(id).subscribe(
      (res:UserEdit[]) => this.form.patchValue(res), error => console.log(error))
    };

  submit(): void {
    this.aSub= this.userService.update(this.form.value,this.route.snapshot.params.id).subscribe(
      res => alert('Save'),
      error => console.log(error.error)
    );
  }

}

