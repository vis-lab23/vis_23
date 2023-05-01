import { Controller, Delete, Get, HttpException, HttpStatus, Logger, Param, Post, Query } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  private readonly logger = new Logger(AppController.name);

  @Get()
  getHello(): string {
    this.logger.log('Get Hello')
    return this.appService.getHello();
  }

  @Get('category')
  async getCategories(@Query('name') name: string) {
    this.logger.log('Get Categories - name: ' + name);
    return name != undefined
    ? await this.appService.getCategoryByName(name)
    : await this.appService.getCategories();
  }

  @Get('category/:id')
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
  async delCategory(@Param('id') id: number) {
    this.logger.log('Delete Categoriy - Id: ' + id);
    await this.appService.delCategory(id);
  }
}
