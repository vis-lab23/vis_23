import { NestFactory } from '@nestjs/core';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { AppModule } from './app.module';
import { Sequelize } from 'sequelize-typescript';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  const config = new DocumentBuilder().setTitle('Category API').setVersion('1.0.0').build();
  const document = SwaggerModule.createDocument(app, config, {deepScanRoutes: true});
  SwaggerModule.setup('openapi', app, document);

  await app.listen(3000);

  const sequelize = app.get(Sequelize);
  // await sequelize.drop();
  try {
    await sequelize.sync();
  } catch (err) {
    console.log(err);
  } 
}
bootstrap();
