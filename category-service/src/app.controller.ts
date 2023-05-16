import { Controller, Delete, Get, Header, HttpException, HttpStatus, Logger, Param, Post, Query } from '@nestjs/common';
import { AppService } from './app.service';
import sequelize, { Transaction } from 'sequelize';
import { Sequelize } from 'sequelize-typescript';
import * as os from 'os';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  private readonly logger = new Logger(AppController.name);

  @Get()
  @Header('x-k8s-pod', os.hostname())
  getHello(): string {
    this.logger.log('Get Hello')
    return this.appService.getHello();
  }

  @Get('category')
  @Header('x-k8s-pod', os.hostname())
  async getCategories(@Query('name') name: string) {
    this.logger.log('Get Categories - name: ' + name);
    return name != undefined
    ? await this.appService.getCategoryByName(name)
    : await this.appService.getCategories();
  }

  @Get('category/:id')
  @Header('x-k8s-pod', os.hostname())
  async getCategory(@Param('id') id: number) {
    this.logger.log('Get Category - Id: ' + id);
    const result = await this.appService.getCategory(id); 
    if (!result) {
      throw new HttpException(
        `Category ${id} does not exist!`,
        HttpStatus.NOT_FOUND,
      );
    }
    return result;
  }

  @Post('category')
  @Header('x-k8s-pod', os.hostname())
  async addCategory(@Query('name') name: string) {
    if (!name) {
      throw new HttpException(
        'Name is missing',
        HttpStatus.BAD_REQUEST,
      );
    }
    this.logger.log('Add Category - name: ' + name);
    await this.appService.addCategory(name);
  }

  @Delete('category/:id')
  @Header('x-k8s-pod', os.hostname())
  async delCategory(@Param('id') id: number) {
    this.logger.log('Delete Categoriy - Id: ' + id);
    await this.appService.delCategory(id);
  }
}
