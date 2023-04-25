import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { SequelizeModule } from '@nestjs/sequelize';
import { Category } from './models/category.model';

@Module({
  imports: [
    SequelizeModule.forRoot({
      dialect: 'mysql',
      host: 'localhost',
      port: 3306,
      username: 'root',
      password: 'c8de110f37300a53a971749',
      database: 'category',
      models: [Category],
    }),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
