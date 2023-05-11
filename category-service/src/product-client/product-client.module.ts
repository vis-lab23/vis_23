import { HttpModule } from '@nestjs/axios';
import { Module } from '@nestjs/common';
import { ProductClientService } from './product-client.service';

@Module({
    imports: [HttpModule],
    providers: [ProductClientService],
    exports: [ProductClientService]
})
export class ProductClientModule {}
