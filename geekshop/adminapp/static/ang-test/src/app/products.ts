export class Category{
  constructor(
    public id:number,
    public name:string,
  ){}
}

export class Products{
  constructor(
  public id: number,
  public name: string,
  public image: string,
  public short_desc: string,
  public description: string,
  public price: string,
  public quantity: number,
  public is_deleted: boolean,
  public created: Date,
  public updated: Date,
  public category: number
  ) {
  }
}
