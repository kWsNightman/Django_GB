export class User{
  constructor(
    public id:bigint,
    public username:string,
    public age:number,
    public first_name:string,
    public last_name:string,
    public email:string,
    public is_staff:boolean,
    public is_active:boolean,
    public is_deleted:boolean,
    public last_login:Date
  ){}
}

export class UserEdit{
  constructor(
    public username:string,
    public first_name:string,
    public last_name:string,
  ){}
}
