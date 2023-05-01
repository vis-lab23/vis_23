import { AutoIncrement, Column, Model, PrimaryKey, Table, Unique } from "sequelize-typescript";

@Table({
    timestamps: false
})
export class Category extends Model {
    @AutoIncrement
    @PrimaryKey
    @Column
    id?: number;

    @Unique
    @Column
    name: string;
}