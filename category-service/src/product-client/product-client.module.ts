import { Module } from '@nestjs/common';
import { ProductClientService } from './product-client.service';

@Module({
    imports: [],
    providers: [ProductClientService],
    exports: [ProductClientService]
})
export class ProductClientModule {}
