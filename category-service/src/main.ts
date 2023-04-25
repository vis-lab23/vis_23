import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { Sequelize } from 'sequelize-typescript';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);

  const sequelize = app.get(Sequelize);
  // await sequelize.drop();
  try {
    await sequelize.sync({ alter: true });
  } catch (err) {
    console.log(err);
  } 
}
bootstrap();
