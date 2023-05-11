import { Logger, Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { SequelizeModule } from '@nestjs/sequelize';
import { Category } from './models/category.model';
import { ConfigModule } from '@nestjs/config';
import { ProductClientModule } from './product-client/product-client.module';

const sequelizeLogger = new Logger(SequelizeModule.name);

@Module({
  imports: [
    ConfigModule.forRoot(),
    SequelizeModule.forRoot({
      dialect: 'mysql',
      host: process.env.DB_HOST,
      port: 3306,
      username: 'root',
      password: 'c8de110f37300a53a971749',
      database: 'category',
      retry: { max: 10 },
      logging: (msg) => sequelizeLogger.debug(msg), 
      models: [Category],
    }),
    SequelizeModule.forFeature([Category]),
    ProductClientModule
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
