import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/sequelize';
import { Category } from './models/category.model';
import { Sequelize } from 'sequelize-typescript';
import { ProductClientService } from './product-client/product-client.service';

@Injectable()
export class AppService {
  constructor(
    @InjectModel(Category)
    private readonly categoryModel: typeof Category,
    private readonly productClient: ProductClientService,
    private readonly sequelize: Sequelize,
  ) { }

  getHello(): string {
    return 'Hello World!';
  }

  async getCategories() {
    return await this.categoryModel.findAll();
  }

  async getCategory(id: number) {
    return await this.categoryModel.findByPk(id);
  }

  async getCategoryByName(name: string) {
    return await this.categoryModel.findOne({
      where: {
        name,
      }
    });
  }

  async addCategory(name: string) {
    await this.categoryModel.create({
      name,
    });
  }

  async delCategory(id: number) {
    await this.productClient.deleteByCategoryId(id);
    await this.categoryModel.destroy({ where: { id } });
  }
}
